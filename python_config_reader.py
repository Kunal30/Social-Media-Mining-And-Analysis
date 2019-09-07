#Code author: Kunal Suthar
#Email: ksuthar1@asu.edu
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser


def read_config(filename='config.twitter.ini', section=None):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section
    twit_dict = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            twit_dict[item[0]] = item[1]
    else:
        raise Exception(
            '{0} not found in the {1} file'.format(section, filename))

    return twit_dict