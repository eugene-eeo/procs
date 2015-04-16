"""
    proclib.response
    ~~~~~~~~~~~~~~~~

    Implements the Response class.
"""


class Response(object):
    """
    A Response object represents the result of running
    a process. The parameters supplied are stored and
    available as attributes as well.

    :param command: The command ran.
    :param process: The `subprocess.Popen` object.
    :param stdout: Output from standard out.
    :param stderr: Output from standard error.
    """

    def __init__(self, command, process, stdout, stderr):
        self.history = []
        self.command = command
        self.process = process
        self.stdout = stdout
        self.stderr = stderr
        self.returncode = process.returncode
        self.pid = process.pid

    @property
    def ok(self):
        """
        Returns a boolean depending on whether the
        `returncode` attribute equals zero.
        """
        return self.returncode == 0

    def __repr__(self):
        if not self.command:
            return '<Response>'
        return '<Response [%s]>' % self.command[0]
