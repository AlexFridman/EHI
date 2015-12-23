from distutils.core import setup

setup(
        name='LabWork1',
        version='',
        package_dir={'LabWork1': '../LabWork1'},
        packages=['LabWork1', 'LabWork1.code', 'LabWork1.code.io', 'LabWork1.code.fibonacci',
                  'LabWork1.code.merge_sort', 'LabWork1.code.quick_sort', 'LabWork1.code.word_count',
                  'LabWork1.code.text_summarizer', 'LabWork1.build.lib.LabWork1', 'LabWork1.tests', 'LabWork1.scripts'],
        scripts=['scripts/main.py'],
        url='',
        license='',
        author='AlexF',
        author_email='',
        description=''
)
