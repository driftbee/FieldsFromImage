class LocalPaths(object):
    def __init__(self, input_dir,
                 output_dir,
                 input_file_name,
                 output_file_name):

        self.input_dir = input_dir

        self.output_dir = output_dir

        self.input_file_name = input_file_name

        self.output_file_name = output_file_name

    def save(self):
        """
        Saves local paths on S3
        :return:
        """

    def load(self):
        """
        Loads paths from S3
        :return:
        """


class S3Paths(object):
    def __init__(self):
        """
        Placeholder
        """

    def save(self):
        """
        Saves local paths on S3
        :return:
        """

    def load(self):
        """
        Loads paths from S3
        :return:
        """