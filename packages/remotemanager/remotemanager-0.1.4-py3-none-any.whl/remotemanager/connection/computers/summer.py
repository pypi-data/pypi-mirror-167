from remotemanager.connection.url import URL
from remotemanager.utils import safe_divide


class Summer(URL):
    """
    subclassed URL specialising in connecting to the CEA Summer HPC
    """

    def __init__(self, **kwargs):

        if kwargs.get('host', None) is not None:
            raise ValueError('cannot change host of dedicated URL')

        kwargs['host'] = 'summer.intra.cea.fr'

        super().__init__(**kwargs)

        self.submitter = 'qsub'

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

        >>> conn = Summer(user='user')
        >>> conn.name = 'dataset_run'
        >>> conn.mpi = 16
        >>> conn.nodes = 2
        >>> conn.omp = 4
        >>> conn.time = '00:30:00'
        >>> conn.queue = 'short'

        Returns (str):
            script
        """

        shebang = '#!/bin/bash'
        pragma = '#PBS'

        if not hasattr(self, 'nodes'):
            nodes = safe_divide(self.mpi, self.max_per_node)
        else:
            nodes = self.nodes

        if not hasattr(self, 'sourcepath'):
            sourcepath = '/W/$USER/build/bigdft/bigdftvars.sh'
        else:
            sourcepath = self.sourcepath

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

source {sourcepath}
export BIGDFT_MPIRUN='mpirun'
export FUTILE_PROFILING_DEPTH=0
"""

        script.append(postscript)

        return '\n'.join(script)
