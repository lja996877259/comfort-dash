<<<<<<< HEAD
import dash_mantine_components as dmc


def my_card(children, span: int | dict = 6, title: str = None, id=None):
    content = []
    if title:
        content.append(dmc.Text(title, mb="xs", fw=700))
    content.append(children)
    if id is not None:
        return dmc.GridCol(dmc.Paper(children=content), span=span, id=id)
    else:
        return dmc.GridCol(dmc.Paper(children=content), span=span)
=======
import dash_mantine_components as dmc

def my_card(children, span: int | dict = 6, title: str = None, id=None):
    content = []
    if title:
        content.append(dmc.Text(title, mb="xs", fw=700))
    content.append(children)
    # return dmc.GridCol(
    #     dmc.Paper(children=content, shadow="xs", p="xs"),
    #     span=span,
    #     id = id
    # )
    if id is not None:
        return dmc.GridCol(
            dmc.Paper(children=content),
            span=span,
            id=id
        )
    else:
        return dmc.GridCol(
            dmc.Paper(children=content),
            span=span
        )
>>>>>>> 07f3ad5a1cf463b5e0160290cc18ee3f2914b8e2
