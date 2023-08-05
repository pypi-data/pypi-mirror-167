"""
This file contains the code for commands that target a bonsai container simulator package in version 2 of the bonsai command line.
"""
__author__ = "Karthik Sankara Subramanian"
__copyright__ = "Copyright 2021, Microsoft Corp."

import click

from json import dumps

from bonsai_cli.exceptions import AuthenticationError, BrainServerError
from bonsai_cli.utils import (
    api,
    get_version_checker,
    raise_as_click_exception,
    raise_client_side_click_exception,
    raise_unique_constraint_violation_as_click_exception,
    raise_brain_server_error_as_click_exception,
)


@click.group()
def container():
    """Container simulator package operations."""
    pass


@click.command("create", short_help="Create a container simulator package.")
@click.option(
    "--name", "-n", help="[Required] Name of the container simulator package."
)
@click.option(
    "--image-uri",
    "-u",
    help="[Required] URI of the container simulator package (container).",
)
@click.option(
    "--cores-per-instance",
    "-r",
    type=float,
    help="[Required] Number of cores that should be allocated for each simulator instance.",
)
@click.option(
    "--memory-in-gb-per-instance",
    "-m",
    type=float,
    help="[Required] Memory in GB that should be allocated for each simulator instance.",
)
@click.option(
    "--os-type",
    "-p",
    help="[Required] OS type for the container simulator package. Windows or Linux.",
    type=click.Choice(["Windows", "Linux"], case_sensitive=False),
)
@click.option(
    "--max-instance-count",
    type=int,
    help="Maximum Number of instances to perform training with the container simulator package.",
)
@click.option(
    "--spot-percent",
    type=click.IntRange(0, 90),
    default=0,
    help="Percentage of maximum instance count of managed simulators that will use spot pricing. Note that the maximum allowed spot percent is 90%",
)
@click.option("--display-name", help="Display name of the container simulator package.")
@click.option("--description", help="Description for the container simulator package.")
@click.option(
    "--workspace-id",
    "-w",
    help="Please provide the workspace id if you would like to override the default target workspace. If your current Azure Active Directory login does not have access to this workspace, you will need to configure the workspace using bonsai configure.",
)
@click.option(
    "--compute-type",
    default="AzureContainerInstance",
    help="(experimental) select the simulator compute infrastructure. choose from [AzureContainerInstance (default) | AzureKubernetesService]",
    hidden=True,
)
@click.option(
    "--debug", default=False, is_flag=True, help="Verbose logging for request."
)
@click.option("--output", "-o", help="Set output, only json supported.")
@click.option(
    "--test",
    default=False,
    is_flag=True,
    help="Enhanced response for testing.",
    hidden=True,
)
@click.pass_context
def create_container_simulator_package(
    ctx: click.Context,
    name: str,
    image_uri: str,
    max_instance_count: int,
    spot_percent: int,
    cores_per_instance: float,
    memory_in_gb_per_instance: float,
    os_type: str,
    display_name: str,
    description: str,
    workspace_id: str,
    compute_type: str,
    debug: bool,
    output: str,
    test: bool,
):
    version_checker = get_version_checker(ctx, interactive=not output)

    error_msg = ""
    required_options_provided = True

    if not name:
        required_options_provided = False
        error_msg += "\nName of the container simulator package is required"

    if not image_uri:
        required_options_provided = False
        error_msg += "\nUri for the container simulator package is required"

    if not cores_per_instance:
        required_options_provided = False
        error_msg += "\nCores per instance for the simulator is required"

    if not memory_in_gb_per_instance:
        required_options_provided = False
        error_msg += "\nMemory in GB per instance for the simulator is required"

    if not os_type:
        required_options_provided = False
        error_msg += "\nOS type for the container simulator package is required"

    if not required_options_provided:
        raise_as_click_exception(error_msg)

    try:
        response = api(use_aad=True).create_sim_package(
            name=name,
            image_path=image_uri,
            max_instance_count=max_instance_count,
            spot_percent=spot_percent,
            cores_per_instance=cores_per_instance,
            memory_in_gb_per_instance=memory_in_gb_per_instance,
            display_name=display_name,
            description=description,
            os_type=os_type,
            package_type="container",
            workspace=workspace_id,
            compute_type=compute_type,
            debug=debug,
            output=output,
        )

        status_message = "Created new container simulator package {}.".format(
            response["name"]
        )

        if output == "json":
            json_response = {
                "status": response["status"],
                "statusCode": response["statusCode"],
                "statusMessage": status_message,
            }

            click.echo(dumps(json_response, indent=4))

        else:
            click.echo(status_message)

    except BrainServerError as e:
        if "Unique index constraint violation" in str(e):
            raise_unique_constraint_violation_as_click_exception(
                debug, output, "Container simulator package", name, test, e
            )
        else:
            raise_brain_server_error_as_click_exception(debug, output, test, e)

    except AuthenticationError as e:
        raise_as_click_exception(e)

    except Exception as e:
        raise_client_side_click_exception(
            output, test, "{}: {}".format(type(e), e.args)
        )

    version_checker.check_cli_version(wait=True, print_up_to_date=False)


container.add_command(create_container_simulator_package)
