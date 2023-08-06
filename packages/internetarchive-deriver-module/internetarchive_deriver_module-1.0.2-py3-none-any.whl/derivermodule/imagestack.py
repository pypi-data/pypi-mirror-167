from pathlib import Path
from os.path import splitext

from subprocess import check_call
from time import time

import zipfile
import tarfile


from .logger import logger

from .metadata import lookup_file_metadata, lookup_file_derivative_path
from .files import canonical_item_filename


def get_imagestack_info_from_format(fmt):
    """
    Attempt to detect if a given format is an image stack format

    Return the image stack format info when the format is an imagestack,
    otherwise None.

    Args:

    * fmt (``str``): format
    """
    if fmt == 'Single Page Processed JP2 ZIP':
        return {'image_type': 'jp2', 'archive_type': 'zip'}
    if fmt == 'Single Page Processed JP2 Tar':
        return {'image_type': 'jp2', 'archive_type': 'tar'}
    if fmt == 'Single Page Processed JPEG ZIP':
        return {'image_type': 'jpg', 'archive_type': 'zip'}
    if fmt == 'Single Page Processed JPEG Tar':
        return {'image_type': 'jpg', 'archive_type': 'tar'}
    if fmt == 'Single Page Processed TIFF ZIP':
        return {'image_type': 'tif', 'archive_type': 'zip'}
    if fmt == 'Single Page Processed TIFF Tar':
        return {'image_type': 'tif', 'archive_type': 'tar'}
    return None


def get_imagestack_info(task_info):
    """
    Reads the source_format from the task information (parse with
    task.get_task_info).

    Returns a dictionary with the following information:

    >>> { 'image_type': 'jp2' or 'jpg' or 'tif', 'archive_type': 'zip' or 'tar'. }
    """
    source_format = task_info['sourceFormat']
    info = get_imagestack_info_from_format(source_format)

    if info is None:
        raise ValueError('Unhandled imagestack format: %s' % source_format)

    return info


def get_imagestack_info_for_file(filename, files_metadata):
    """
    Reads the filename format from the files metadata and returns the imagestack
    info

    Returns a dictionary with the following information:

    >>> { 'image_type': 'jp2' or 'jpg' or 'tif', 'archive_type': 'zip' or 'tar'. }
    """
    file_md = lookup_file_metadata(files_metadata, filename)
    source_format = file_md['format']
    info = get_imagestack_info_from_format(source_format)

    if info is None:
        raise ValueError('Unhandled imagestack format: %s' % source_format)

    return info


def get_source_image_stack_for_file(source_file, files_metadata):
    """
    Find the source image stack for a given source_file, by searching the files
    metadata derivative tree.

    Args:

    * source_file (``str``): canonical filename
    * files_metadata: files metadata as returned by `load_files_metadata`.

    Returns: ``str`` (the filename of the image stack) or ``None``.
    """
    source_file = source_file
    file_derivative_path = lookup_file_derivative_path(files_metadata, source_file)

    for filename in file_derivative_path:
        file_md = lookup_file_metadata(files_metadata, filename)
        file_format = file_md['format']

        imagestack_info = get_imagestack_info_from_format(file_format)
        if imagestack_info is not None:
            return filename

    return None


def unpack_and_validate_imagestack(imagestack_path, imagestack_info, dst):
    """Unpack and validate an imagestack

    An imagestack is valid if it contains at least one directory that contains
    at least one image of the expected image type.

    Unless you need all the images written to disk (which could be slow and take
    up space), it would be better to look at the iterate_imagestack and
    validate_imagestack methods in this module.

    Args:

    * imagestack_path (``str``): The imagestack archive path
    * imagestack_info (``dict``)::

        >>> {'archive_type': ..., 'image_type': ...}

    * dst (``str``): Destination directory for the unpacked imagestack

    Returns:

    * ``(str, int)``: Tuple containing the path to the unpacked image directory
                      and the image count.
    """
    logger.info('Unpacking image stack.')
    start_time = time()
    if imagestack_info['archive_type'] == 'tar':
        check_call(['tar', '-xf', imagestack_path, '-C', dst])
    elif imagestack_info['archive_type'] == 'zip':
        check_call(['unzip', '-qq', '-o', imagestack_path, '-d', dst])
    else:
        raise ValueError('Cannot extract archive_type %s' % imagestack_info['archive_type'])
    logger.info('Unpacking image stack took %f seconds', time() - start_time)

    for f in Path(dst).iterdir():
        if f.name.endswith(f'_{imagestack_info["image_type"]}'):
            img_dir = f
            break
    else:
        raise Exception('Unable to locate image directory in imagestack.')

    image_count = 0
    for img_path in img_dir.iterdir():
        if img_path.suffix[1:] == imagestack_info['image_type']:
            image_count += 1

    if image_count == 0:
        raise Exception('Imagestack contains no valid images.')

    return str(img_dir), image_count


def iterate_imagestack(imagestack_path, imagestack_info, sort=True):
    """Unpack and validate an imagestack

    An imagestack is valid if it contains at least one directory that contains
    at least one image of the expected image type. All operations are done
    without writing to the disk.

    Args:

    * imagestack_path (``str``): The imagestack archive path
    * imagestack_info (``dict``)::

        >>> {'archive_type': ..., 'image_type': ...}

    * sort (``bool``): optional, sort the files by name (sort=False should be
                       faster if you don't care about the order)

    Returns:

    * Iterator of (filename, file handle)
    """
    if imagestack_info['archive_type'] == 'tar':
        tf = tarfile.open(imagestack_path)

        members = tf.getmembers()
        if sort:
            members = sorted(members, key=lambda x: x.name)

        for idx, img in enumerate(members):
            if not img.isfile():
                continue

            ci = tf.extractfile(img)

            yield img.name, ci

            ci.close()

        tf.close()

    elif imagestack_info['archive_type'] == 'zip':
        zf = zipfile.ZipFile(imagestack_path)
        namelist = zf.namelist()

        if sort:
            namelist = sorted(namelist)

        for idx, img in enumerate(namelist):
            info = zf.getinfo(img)
            if info.is_dir():
                continue
            ci = zf.open(img)

            yield info.filename, ci

            ci.close()

        zf.close()
    else:
        raise ValueError('Cannot extract archive_type %s' % imagestack_info['archive_type'])

    return


def validate_imagestack(imagestack_path, imagestack_info):
    """
    Validate an imagestack given a path. An imagestack is valid if it contains
    at least image with a supported image type. All operations are done without
    writing to the disk.

    Args:

    * imagestack_path (``str``): The imagestack archive path
    * imagestack_info (``dict``)::

        >>> {'archive_type': ..., 'image_type': ...}

    If the method does not raise an Exception, the image stack is valid.
    """
    image_count = 0

    for img_path, _ in iterate_imagestack(imagestack_path, imagestack_info):
        _, file_extension = splitext(img_path)

        if file_extension[1:] == imagestack_info['image_type']:
            image_count += 1

    if image_count == 0:
        raise Exception('Imagestack contains no valid images.')

    return
