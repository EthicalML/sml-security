from pydantic import BaseSettings


HUGGINGFACE_TASK_TAG = "task"

ENV_PREFIX_{{ cookiecutter.class_name.upper() }}_SETTINGS = "MLSERVER_MODEL_{{ cookiecutter.class_name.upper() }}_"
HUGGINGFACE_PARAMETERS_TAG = "huggingface_parameters"
PARAMETERS_ENV_NAME = "PREDICTIVE_UNIT_PARAMETERS"


class {{ cookiecutter.class_name }}Settings(BaseSettings):
    """
    Parameters that apply only to alibi huggingface models
    """

    class Config:
        env_prefix = ENV_PREFIX_{{ cookiecutter.class_name.upper() }}_SETTINGS

    lambda_value: str = ""

