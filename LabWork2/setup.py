from distutils.core import setup

setup(
    name='LabWork2',
    version='',
    package_dir={'LabWork2': '../LabWork2'},
    packages=['LabWork2', 'LabWork2.code', 'LabWork2.code.logger', 'LabWork2.code.vector', 'LabWork2.code.xrange',
              'LabWork2.code.filterable_list', 'LabWork2.code.json_serializer', 'LabWork2.code.linear_function',
              'LabWork2.code.json_attr_loader_meta', 'LabWork2.code.cached_decorator', 'LabWork2.code.ext_mem_merge_sort',
              'LabWork2.code.singleton_metaclass', 'LabWork2.code.recursive_defaultdict',
              'LabWork2.code.model_creator_metaclass', 'LabWork2.tests', 'LabWork2.tests.logger',
              'LabWork2.tests.vector', 'LabWork2.tests.xrange', 'LabWork2.tests.filterable_list',
              'LabWork2.tests.json_serializer', 'LabWork2.tests.linear_function', 'LabWork2.tests.cached_decorator',
              'LabWork2.tests.ext_mem_merge_sort', 'LabWork2.tests.singleton_metaclass',
              'LabWork2.tests.json_attr_loader_meta', 'LabWork2.tests.recursive_defaultdict',
              'LabWork2.tests.model_creator_metaclass'],
    url='',
    license='',
    author='AlexF',
    author_email='',
    description='', requires=['numpy', 'numpy']
)
