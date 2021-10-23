if __name__ == "__main__":
    # import logging
    #
    # logging.basicConfig(filename='logging1.log', encoding='utf-8', level=logging.DEBUG)
    # logging.debug('This message should go to the log file')
    # logging.info('So should this')
    # logging.warning('And this, too')
    # logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
    #
    # with open('logging1.log', 'r') as f:
    #     print(f'File Contents: \n{f.read()}')

    import logging

    LOG_FILENAME = '/tmp/logging_example.out'
    # LOG_FILENAME = 'example.log'
    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
    logging.debug('This message should go to the log file')
