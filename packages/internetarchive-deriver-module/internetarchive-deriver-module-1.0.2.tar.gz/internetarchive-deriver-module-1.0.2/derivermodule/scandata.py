import tempfile
import zipfile
from subprocess import check_call
from pathlib import Path

import xmltodict

from .const import PB_ITEM, PB_TMP
from .logger import logger


def get_scandata_xml(identifier, source_file):
    """
    Parses the scandata.xml file for a given identifier and source_file.

    Args:

    * identifier (``str``): Identifier of the item
    * source_file (``str``): sourceFile to be operated on

    Returns:

    * Path to the scandata (``str``) or None
    """
    item_dir = Path(PB_ITEM)

    zip_path = item_dir/'scandata.zip'
    raw_xml_path = item_dir/'scandata.xml'
    if source_file:
        if source_file.endswith('page_numbers.json'):
            source_xml_path = Path(f'{source_file[:-18]}_scandata.xml')
        else:
            source_xml_path = Path(f'{source_file.rsplit("_", 1)[0]}_scandata.xml')

    if source_xml_path.exists():
        return str(source_xml_path)
    elif raw_xml_path.exists():
        return str(raw_xml_path)
    elif zip_path.exists():
        try:
            # XXX: We don't clean up the temporary directory when we're done,
            # since the Docker container will remove all files upon completion.
            directory = tempfile.mkdtemp(dir=PB_TMP)
            xml_path = Path(directory)/'scandata.xml'

            zf = zipfile.ZipFile(zip_path)
            sf = zf.open('scandata.xml')
            f = open(xml_path, 'wb+')
            f.write(sf.read())
            f.close()
            sf.close()
            zf.close()

            assert(xml_path.exists())
        except Exception as e:
            logger.warning('Unable to extract scandata.xml from scandata.zip')
            logger.exception(e)
            return None

        return str(xml_path)

    logger.warning(f'Unable to find scandata file')
    return None


def scandata_parse(scandata_path):
    """
    Parse scandata.xml to native Python format

    Args:

    * scandata_path (``str``): Path to the scandata

    Returns:

    * Scandata as dictionary
    """
    scandata = xmltodict.parse(open(scandata_path, 'rb').read())
    return scandata


def scandata_get_page_count(scandata):
    """
    Get the number of page elements in a parsed scandata object

    Args:

    * scandata (``dict``): Scandata as returned by `scandata_parse`.

    Returns:

    * The number of page elements (``int``)
    """
    pages = scandata.get('book', {}).get('pageData', {}).get('page', [])
    if not isinstance(pages, list):
        pages = [pages]

    return len(pages)


def scandata_get_skip_pages(scandata):
    """
    Returns a list of indexes of pages in scandata.xml that have
    addToAccessFormats = false

    Args:

    * scandata: Parsed scandata as returned by scandata_parse

    Returns:

    * Indexes of pages that should not added to access formats
      (``list of int``)
    """
    skip = []

    pages = scandata['book']['pageData']['page']

    # If there is just one page, pages is not a list.
    if not isinstance(pages, list):
        pages = [pages]

    for idx in range(len(pages)):
        try:
            add_to_access_format = pages[idx]['addToAccessFormats']
            if add_to_access_format == 'false':
                skip.append(idx)
        except KeyError:
            pass

    return skip
