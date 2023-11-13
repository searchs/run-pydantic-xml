import xml.etree.ElementTree as ET
from loguru import logger

logger.info("Running XML Reader")

tree = ET.parse("data/movie.xml")
root = tree.getroot()

if __name__ == "__main__":
    logger.info(f"Root TAG: {root.tag}")
    logger.info(f"Root ATTR: {root.attrib}")
    for child in root:
        logger.info(f"{child.tag, child.attrib}")
        # print(child.tag, child.attrib)
    all = [elem.tag for elem in root.iter()]
    logger.info(f"{all}")

    # print(ET.tostring(root,encoding='utf8').decode('utf8'))

    for movie in root.iter("movie"):
        print(movie.attrib)

    for description in root.iter("description"):
        print(description.text)
