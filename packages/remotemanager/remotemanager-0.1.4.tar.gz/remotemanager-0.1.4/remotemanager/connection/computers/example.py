from remotemanager.connection.url import URL
from remotemanager.utils import safe_divide


class Example_Computer(URL):
    """
    example class for connecting to a remote computer
    """

    def __init__(self, **kwargs):

        if kwargs.get('host', None) is not None:
            raise ValueError('cannot change host of dedicated URL')

        kwargs['host'] = 'remote.address.for.connection'

        super().__init__(**kwargs)

        self.submitter = 'submit_command'

    @property
    def ssh(self):
        """
        Returns (str):
            modified ssh string for Summer avoiding perl error
        """
        return 'LANG=C ' + super().ssh

    @property
    def script(self):
        """
        Returns the base script required for a run on this computer
        Required values should be set prior to passing to Dataset

        Returns (str):
            script
        """

        shebang = '#!/bin/bash'
        pragma = '#PBS'

        if not hasattr(self, 'nodes'):
            nodes = safe_divide(self.mpi, self.max_per_node)
        else:
            nodes = self.nodes

        options = {'-N': self.name,
                   '-q': self.queue,
                   '-o': f'{self.name}-stdout',
                   '-e': f'{self.name}-stderr',
                   '-l': f'nodes={nodes}:'
                         f'ppn={self.mpi},'
                         f'walltime={self.time}'}

        modules = ['icc',
                   'impi',
                   'mkl/18',
                   'python/anaconda3']

        script = [shebang]

        for flag, value in options.items():
            script.append(f'{pragma} {flag} {value}')

        script.append('')
        for module in modules:
            script.append(f'module load {module}')

        postscript = f"""
cd $PBS_O_WORKDIR
export OMP_NUM_THREADS={self.omp}
"""

        script.append(postscript)

        return '\n'.join(script)
