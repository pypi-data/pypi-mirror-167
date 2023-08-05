import logging as _logging
import os as _os
import sys as _sys

import click as _click
from gnssanalysis import gn_diffaux as _gn_diffaux


def diffutil_verify_input(input):
    #     log_lvl = 40 if atol is None else 30 # 40 is error, 30 is warning. Constant tolerance differences are reported as warnings
    if input is None:
        _click.echo(f"Error: Missing '-i' / '--input' arguments.")
        _sys.exit(-1)
    for i in range(len(input)):
        if (input[i]) is None:
            _click.echo(f"Error: Missing argument {i} of '-i' / '--input'.")
            _sys.exit(-1)
        _click.Path(exists=True)(input[i])


    _logging.getLogger().setLevel(_logging.INFO)
    _logging.info(f":diffutil ========== STARTING DIFFUTIL ==========")
    _logging.info(f":diffutil input1: {_os.path.abspath(input[0])}")
    _logging.info(f":diffutil input2: {_os.path.abspath(input[1])}")


def diffutil_verify_status(status, passthrough):
    if status:
        if not passthrough:
            _logging.error(msg=f":diffutil failed. Calling sys.exit\n")
            _sys.exit(status)
        else:
            _logging.info(
                msg=f":diffutil failed but no sys.exit as passthrough enabled\n"
            )
    else:
        _logging.info(":diffutil [ALL OK]")


def get_filetype(path):
    """
    Returns a suffix of a file from a path,
    Uses a dict to correct for known suffix issues file types.
    If not present in dict -> return suffix as extracted.
    Also, strips out the underscore-appended part of the suffix, e.g. _smoothed.
    """
    basename = _os.path.basename(path)
    suffix = basename.split(".")[1].lower().partition('_')[0]
    filetype_dict = {"snx": "sinex", "sum": "trace", "eph": "sp3"}
    if suffix in filetype_dict.keys():
        return filetype_dict[suffix]
    elif suffix == "out":
        return basename[:3]
    elif suffix[:2].isdigit and suffix[2] == "i":
        return "ionex"
    return suffix


@_click.group(invoke_without_command=True)
@_click.option(
    "-i",
    "--input",
    nargs=2,
    type=str,
    help="path to compared files, can be compressed with LZW (.Z) or gzip (.gz). Takes exactly two arguments",
)
@_click.option(
    "--passthrough",
    is_flag=True,
    help="return 0 even if failed. Useful for pipeline runs",
)
@_click.option(
    "-a",
    "--atol",
    type=float,
    default=None,
    help="absolute tolerance",
    show_default=True,
)
@_click.option("-c", "--coef", type=float, default=1, help="std coefficient")
@_click.option("-l", "--log_lvl", type=int, default=40, help="logging level selector")
@_click.pass_context
def diffutil(ctx, input, passthrough, atol, coef, log_lvl):
    if ctx.invoked_subcommand is None:
        filetype = get_filetype(input[0])
        _logging.info(
            f":diffutil invoking '{filetype}' command based on the extension of the first argument of the input"
        )
        ctx.invoke(diffutil.commands[filetype])
    else:
        _logging.info(f":diffutil invoking {ctx.invoked_subcommand} command")


@diffutil.command()
@_click.pass_context
@_click.option("-p", "--plot", is_flag=True, default=False, help="produce plots")
def trace(ctx, plot):
    diffutil_verify_input(ctx.parent.params["input"])
    status = _gn_diffaux.difftrace(
        trace1_path=ctx.parent.params["input"][0],
        trace2_path=ctx.parent.params["input"][1],
        tol=ctx.parent.params["atol"],
        std_coeff=ctx.parent.params["coef"],
        log_lvl=ctx.parent.params["log_lvl"],
        plot=plot,
    )
    diffutil_verify_status(status=status, passthrough=ctx.parent.params["passthrough"])


@diffutil.command()
@_click.pass_context
def sinex(ctx):
    diffutil_verify_input(ctx.parent.params["input"])
    status = _gn_diffaux.diffsnx(
        snx1_path=ctx.parent.params["input"][0],
        snx2_path=ctx.parent.params["input"][1],
        tol=ctx.parent.params["atol"],
        std_coeff=ctx.parent.params["coef"],
        log_lvl=ctx.parent.params["log_lvl"],
    )
    diffutil_verify_status(status=status, passthrough=ctx.parent.params["passthrough"])


@diffutil.command()
@_click.pass_context
def ionex(ctx):
    diffutil_verify_input(ctx.parent.params["input"])
    status = _gn_diffaux.diffionex(
        ionex1_path=ctx.parent.params["input"][0],
        ionex2_path=ctx.parent.params["input"][1],
        tol=ctx.parent.params["atol"],
        std_coeff=ctx.parent.params["coef"],
        log_lvl=ctx.parent.params["log_lvl"],
    )
    diffutil_verify_status(status=status, passthrough=ctx.parent.params["passthrough"])


@diffutil.command()
@_click.pass_context
def stec(ctx):
    diffutil_verify_input(ctx.parent.params["input"])
    status = _gn_diffaux.diffstec(
        path1=ctx.parent.params["input"][0],
        path2=ctx.parent.params["input"][1],
        tol=ctx.parent.params["atol"],
        std_coeff=ctx.parent.params["coef"],
        log_lvl=ctx.parent.params["log_lvl"],
    )
    diffutil_verify_status(status=status, passthrough=ctx.parent.params["passthrough"])


@diffutil.command()
@_click.pass_context
# @_click.option() bias norm type, also no coef
def clk(ctx):
    diffutil_verify_input(ctx.parent.params["input"])
    status = _gn_diffaux.diffclk(
        clk_a_path=ctx.parent.params["input"][0],
        clk_b_path=ctx.parent.params["input"][1],
        tol=ctx.parent.params["atol"],
        log_lvl=ctx.parent.params["log_lvl"],
    )
    diffutil_verify_status(status=status, passthrough=ctx.parent.params["passthrough"])


@diffutil.command()
@_click.pass_context
@_click.option(
    "--aux1",
    type=_click.Path(exists=True),
    default=None,
    help="path to aux1 file",
    show_default=True,
)
@_click.option(
    "--aux2",
    type=_click.Path(exists=True),
    default=None,
    help="path to aux2 file",
    show_default=True,
)
@_click.option("-p", "--plot", is_flag=True, help="outputs a plot to terminal")
def sp3(ctx, aux1, aux2, plot):  # no coef
    diffutil_verify_input(ctx.parent.params["input"])
    status = _gn_diffaux.diffsp3(
        sp3_a_path=ctx.parent.params["input"][0],
        sp3_b_path=ctx.parent.params["input"][1],
        clk_a_path=aux1,
        clk_b_path=aux2,
        tol=ctx.parent.params["atol"],
        log_lvl=ctx.parent.params["log_lvl"],
        plot=plot,
    )
    diffutil_verify_status(status=status, passthrough=ctx.parent.params["passthrough"])


@diffutil.command()
@_click.pass_context
def pod(ctx):  # no coef
    diffutil_verify_input(ctx.parent.params["input"])
    status = _gn_diffaux.diffpodout(
        pod_out_a_path=ctx.parent.params["input"][0],
        pod_out_b_path=ctx.parent.params["input"][1],
        tol=ctx.parent.params["atol"],
        log_lvl=ctx.parent.params["log_lvl"],
    )
    diffutil_verify_status(status=status, passthrough=ctx.parent.params["passthrough"])


@_click.command()
@_click.option(
    "--sp3_a",
    required=True,
    type=_click.Path(exists=True),
    help="path to the main sp3 file which will be used to interpolate velocities and compute RAC rotation matrix",
)
@_click.option(
    "--sp3_b",
    required=True,
    type=_click.Path(exists=True),
    help="path to another sp3 file",
)
@_click.option(
    "-hlm",
    "--hlm_mode",
    type=_click.Choice(["None", "ECF", "ECI"], case_sensitive=False),
    help="helmert inversion mode",
    default="None",
    show_default=True,
)
@_click.option(
    "-o",
    "--output",
    type=_click.Path(exists=False),
    help="plot output path",
    default=None,
    show_default=True,
)
def sp3compare(sp3_a, sp3_b, hlm_mode, output):
    """Compares two sp3 files and outputs RAC residuals plot. Sp3 files can be LZW (.Z) or Gzip (.gz) compressed. If -hlm parameter provided, will do the helmert transormation of sp3_b file into the frame of sp3_a and append sp3_b residuals plot to the bottom. The helmert inversion mode is used to selected at which step to do the parameter computation and transfomation: ECF (as in sp3) or ECI."""

    from gnssanalysis import gn_io as _gn_io
    from gnssanalysis import gn_plot as _gn_plot

    sp3_a = _gn_io.sp3.read_sp3(sp3_a)
    sp3_b = _gn_io.sp3.read_sp3(sp3_b)
    if hlm_mode == "None":
        hlm_mode = None
    rac = _gn_io.sp3.diff_sp3_rac(sp3_a, sp3_b, hlm_mode=hlm_mode)
    _gn_plot.racplot(rac=rac, output=output)


@_click.command()
@_click.argument("sinexpaths", required=True, nargs=-1, type=_click.Path(exists=True))
@_click.option(
    "-o", "--outdir", type=_click.Path(exists=True), help="output dir", default=None
)
def snxmap(sinexpaths, outdir):
    """Creates sinex station map html. Parses sinex SITE/ID block and create an html map.
    Expects paths to sinex files (.snx/.ssc). Can also be compressed with LZW (.Z)"""
    from gnssanalysis import gn_io as _gn_io, gn_plot as _gn_plot

    size = 0.5
    _logging.getLogger().setLevel(_logging.INFO)
    _logging.info(msg=sinexpaths)
    id_df = _gn_io.sinex.gather_snx_id(sinexpaths, add_markersize=True, size=size)
    _gn_plot.id_df2html(id_df=id_df, outdir=outdir, verbose=True)


@_click.command()
@_click.option(
    "-s", "--sp3paths", required=True, multiple=True, type=_click.Path(exists=True)
)
@_click.option(
    "-c",
    "--clkpaths",
    required=False,
    multiple=True,
    type=_click.Path(exists=True),
    default=None,
)
@_click.option(
    "-o",
    "--output",
    type=_click.Path(exists=True),
    help="output path",
    default=_os.curdir + "/merge.sp3",
)
def sp3merge(sp3paths, clkpaths, output):
    """
    sp3 files paths to merge, Optional clock files which is useful to insert clk offset values into sp3 file.
    """
    from gnssanalysis import gn_io as _gn_io

    _logging.info(msg=output)
    merged_df = _gn_io.sp3.sp3merge(sp3paths=sp3paths, clkpaths=clkpaths)
    _gn_io.sp3.write_sp3(sp3_df=merged_df, path=output)


@_click.command()
@_click.option(
    "-l", "--logglob", required=True, type=str, help="logs glob path (required)"
)
@_click.option("-r", "--rnxglob", type=str, help="rinex glob path")
@_click.option(
    "-o", "--output", type=str, help="rinex glob path", default="./metagather.snx"
)
@_click.option(
    "-fs",
    "--framesnx",
    type=_click.Path(exists=True),
    help="frame sinex path",
    default=None,
)
@_click.option(
    "-fd",
    "--frame_dis",
    type=_click.Path(exists=True),
    help="frame discontinuities file path (required with --frame_snx)",
    default=None,
)
@_click.option(
    "-fp",
    "--frame_psd",
    type=_click.Path(exists=True),
    help="frame psd file path",
    default=None,
)
@_click.option(
    "-d",
    "--datetime",
    help="date to which project frame coordinates, default is today",
    default=None,
)
@_click.option(
    "-n",
    "--num_threads",
    type=int,
    help="number of threads to run in parallel",
    default=None,
)
def log2snx(
    logglob, rnxglob, outfile, frame_snx, frame_dis, frame_psd, datetime, num_threads
):
    """
    IGS log files parsing utility. Globs over log files using LOGGLOB expression
     and outputs SINEX metadata file. If provided with frame and frame discontinuity files (soln),
    will project the selected stations present in the frame to the datetime specified.

    How to get the logfiles:

    rclone sync igs:pub/sitelogs/ /data/station_logs/station_logs_IGS -vv

    How to get the frame files:

    rclone sync itrf:pub/itrf/itrf2014 /data/ITRF/itrf2014/ -vv --include "*{gnss,IGS-TRF}*" --transfers=10

    rclone sync igs:pub/ /data/TRF/ -vv --include "{IGS14,IGb14,IGb08,IGS08}/*"

    see rclone config options inside this script file
    Alternatively, use s3 bucket link to download all the files needed s3://peanpod/aux/

    install rclone with curl https://rclone.org/install.sh | sudo bash -s beta

    rclone config file (content from rclone.conf):

    \b
    [cddis]
    type = ftp
    host = gdc.cddis.eosdis.nasa.gov
    user = anonymous
    pass = somerandomrandompasswordhash
    explicit_tls = true

    \b
    [itrf]
    type = ftp
    host = itrf-ftp.ign.fr
    user = anonymous
    pass = somerandomrandompasswordhash

    \b
    [igs]
    type = ftp
    host = igs-rf.ign.fr
    user = anonymous
    pass = somerandomrandompasswordhash
    """
    from gnssanalysis import gn_io as _gn_io

    if isinstance(rnxglob, list):
        if (len(rnxglob) == 1) & (
            rnxglob[0].find("*") != -1
        ):  # it's rnx_glob expression (may be better to check if star is present)
            rnxglob = rnxglob[0]

    _gn_io.igslog.write_meta_gather_master(
        logs_glob_path=logglob,
        rnx_glob_path=rnxglob,
        out_path=outfile,
        frame_snx_path=frame_snx,
        frame_soln_path=frame_dis,
        frame_psd_path=frame_psd,
        frame_datetime=datetime,
        num_threads=num_threads,
    )
