"""Output using matplotlib."""
import warnings
from typing import Tuple

from matplotlib import pyplot
from tunable import Tunable

from ..parameters import Height, Width
from ..simulation.simulator import World
from . import Output, check_overwrite, ensure_path_and_extension_and_number


class MicrometerPerCm(Tunable):
    default: float = 2.5


class PlotRenderer(Output, Output.Default):
    """Output using matplotlib."""

    def __init__(self):
        super().__init__()

        self.fig = self.ax = None

    def output(self, world: World, **kwargs) -> Tuple[pyplot.Figure, pyplot.Axes]:
        if self.fig is None:
            self.fig = pyplot.figure(
                figsize=(
                    Width.value / MicrometerPerCm.value / 2.51,
                    Height.value / MicrometerPerCm.value / 2.51,
                )
            )

        fig = self.fig

        if self.ax is None:
            self.ax = fig.add_subplot(111)

        ax = self.ax

        ax.clear()

        for cell in world.cells:
            points = cell.points_on_canvas()
            ax.plot(points[:, 0], points[:, 1])

        for boundary in world.boundaries:
            for start, stop in zip(boundary, boundary[1:]):
                ax.plot([start[0], stop[0]], [start[1], stop[1]])

        ax.set_xlim(0, Width.value)
        ax.set_ylim(0, Height.value)
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            pyplot.tight_layout()

        return fig, ax

    def write(
        self,
        world: World,
        file_name: str,
        output_count: int = 0,
        overwrite: bool = False,
        **kwargs
    ) -> None:
        fig, ax = self.output(world)

        extensions = ['.png'] + [
            '.' + extension
            for extension in fig.canvas.get_supported_filetypes().keys()
            if extension != 'png'
        ]

        fig.savefig(
            check_overwrite(
                ensure_path_and_extension_and_number(
                    file_name, extensions, output_count
                ),
                overwrite=overwrite,
            )
        )

    def display(self, world: World, **kwargs) -> None:
        if self.fig:
            if not pyplot.fignum_exists(self.fig.number):
                raise KeyboardInterrupt

        pyplot.ion()
        self.output(world)
        pyplot.show()
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()


__all__ = ['PlotRenderer', 'MicrometerPerCm']
