from array import array
from typing import Dict
from runfalconbuildtools.artifacts import Artifact, ArtifactsManager, DummyArtifact, JmeterArtifact
from runfalconbuildtools.file_utils import copy_file
from runfalconbuildtools.logger import Logger

class MainCommand:

    def __init__(self, command:str, operation:str, args:array = []):
        self.command = command
        self.operation = operation
        self.args = args

    def to_string(self) -> str:
        args:str = ' '
        for arg in self.args:
            args += '{key}="{value}" '.format(key = arg['key'], value = arg['value'])
        return self.command + ' ' + self.operation + args

    def get_argument(self, arg_name:str) -> Dict:
        filtered_args:array = list(filter(lambda arg : arg['key'] == arg_name, self.args))
        return filtered_args[0]['value'] if len(filtered_args) > 0 else None

class ModuleMain:

    logger:Logger = Logger('ModuleMain')

    usage_message:str = \
                    'Use python -m runfalconbuildtools <command> <operation> [args..]\n\n' + \
                    'Commands:\n' + \
                    '\tartifact: Access to runfalconbuildtools artifacts\n' + \
                    '\t\tOperations:\n' + \
                    '\t\t\tget: Download an specific artifact.  Arguments:\n' + \
                    '\t\t\t\tname=<artifact name>: Name of the artifact to download.\n' + \
                    '\t\t\t\tvresion=<version>: Artifact version to download\n' + \
                    '\t\t\t\tout=<output directory>: Directory where the artifact will be saved\n\n' + \
                    '\t\t\t\tExample: python -m runfalconbuildtools artifact get name="my-artifact" version="1.0.0" out="./my_artifact.zip"'

    def __init__(self, commnad_args:array):
        self.command_args = commnad_args

    def __create_arg(self, str_arg:str) -> Dict:
        index:int = str_arg.find('=')
        
        if index < 0:
            raise Exception('Invalid argument: {arg}\n\n{usage}'.format(arg = str_arg, usage = self.usage_message))

        key:str = str_arg[0:index]
        value:str = str_arg[index + 1 : len(str_arg)].strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1 : len(value) - 1]

        return {'key': key, 'value': value}

    def __get_command(self) -> MainCommand:
        if (self.command_args == None):
            raise Exception('No command args')

        if (len(self.command_args) < 2):
            raise Exception('Invalid comman.\n\n' + self.usage_message)

        args:array = []
        for arg in self.command_args[2:len(self.command_args)]:
            args.append(self.__create_arg(arg))

        main_command:MainCommand = MainCommand(self.command_args[0], self.command_args[1], args)
        return main_command

    def __get_artifact(self, main_command:MainCommand):
        output_path:str = None
        artifact:Artifact = None

        artifact_name:str = main_command.get_argument('name')
        match artifact_name:
            case 'dummy':
                artifact = DummyArtifact()
            case 'jmeter':
                artifact = JmeterArtifact()
            case _:
                raise Exception('Invalid artifact name "{artifact}"'.format(artifact = artifact_name))

        artifacts_version = main_command.get_argument('version')
        artifacts_manager:ArtifactsManager = ArtifactsManager()
        output_path = artifacts_manager.get_artifact(artifact, main_command.get_argument(artifacts_version))
        target_path = main_command.get_argument('out')
        copy_file(output_path, target_path)

        self.logger.info('Artifact "{artifact}" version "{version}" successfully downloaded to "{out}"'
                        .format(artifact = artifact_name, version = artifacts_version, out = target_path))

    def __run_artifact(self, main_command:MainCommand):
        match main_command.operation:
            case 'get':
                self.__get_artifact(main_command)

    def __run(self, main_command:MainCommand):
        match main_command.command:
            case 'artifact':
                self.__run_artifact(main_command)

    def run(self):
        main_command:MainCommand = self.__get_command()
        self.__run(main_command)

