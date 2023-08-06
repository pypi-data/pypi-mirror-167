import pandas as pd
import typing as typ

from pacifico_devel.util.reportTemplate.src.core.Plot.Table.Table import Table
from pacifico_devel.util.reportTemplate.src.core.Plot.Plot import MultiDisplay
from pacifico_devel.util.reportTemplate.src.util.PacificoPlotColors import PacificoPlotColors
import pacifico_devel.util.reportTemplate.src.util.Enumerations as renm


class TableDataframeImage(Table):

    def makePlot(self,
                 df: pd.DataFrame,
                 shape: typ.Tuple[int, int],
                 title: typ.Optional[str] = None,
                 backend: typ.Union[str, renm.Backend, None] = None,
                 formatter: dict = None) -> MultiDisplay:
        dfAux = self._translateDataFrame(df)
        thProps = [("background-color", PacificoPlotColors.BLUE.getCodeString()),
                   ("color", "white"), ('font-family', 'Klartext Mono'), ('text-align', 'center'),
                   ('font-size', '14pt')]

        tdProps = [('font-family', 'Klartext Mono'), ('font-size', '14pt')]

        dfst = dfAux.style.set_table_styles([{"selector": "th", "props": thProps},
                                             {"selector": "td", "props": tdProps}])

        if formatter is None:
            dfst = dfst.format("{:.2f}")
        else:
            dfst = dfst.format(formatter)
        # print(dfst.to_html())

        self._saveImageFile(dfst)
        return dfst


if __name__ == '__main__':
    from pacifico_devel.util.reportTemplate.src.util.testing import makeRandomCategoricalDf

    df = makeRandomCategoricalDf(shape=(20, 3))

    tdi = TableDataframeImage()
    tdi.makePlot(df=df,
                 title="",
                 backend="bokeh",
                 shape=(1, 1 / 2))
