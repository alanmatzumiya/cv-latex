from json import load
from os import listdir, system
from os.path import join


class Template:
    path = "./templates"
    data = dict(
        docs={i.split(".")[0]: join("./templates", i) for i in listdir("./docs")},
        img={i.split(".")[0]: join("./templates", i) for i in listdir("./img")},
        templates={i.split(".")[0]: join("./templates", i) for i in listdir(path)}
    )
    cfg = load(open("info.json"))

    def get(self, name):
        data = open(self.data["templates"][name]).read()
        for key, value in self.cfg.items():
            if type(value) == str:
                data = data.replace(f"<{key.upper()}>", value)
        data = data.replace(
            "<APTITUDES>", "\cvtext{" + "".join([
                r'\textbf{- ' + i + r'}\\' for i in self.cfg["aptitudes"]
            ]) + "}"
        )
        data = data.replace(
            "<SKILLS>", "\n".join([
                '\cvskill{' + f'{x["name"]}' + "}{" + x["years"] + "+ yrs}{" + x["scale"] + r'} \\[-2pt]'
                for x in self.cfg["skills"]
            ])
        )
        data = data.replace(
            "<EDUCATION>", "\n".join(
                "".join([r"\cvmetaevent",
                "{" + x["period"] + "}",
                "{" + x["name"] + "}",
                r"{\textbf{" + x["institution"] + "}}",
                "{\cvlist{\item " + x["description"],
                " \href{" + x["href"] + r"}{\textbf{Informacion Aqui}}.}" if x["href"] else ".}",
                "}"
                ]) for x in self.cfg["education"]
            )
        )
        data = data.replace(
            "<EXPERIENCE>", "\n\n".join(
                "".join([
                    r"\cvevent",
                    "{" + x["period"] + "}",
                    "{" + x["name"] + "}",
                    "{" + x["place"] + "}",
                    "{\cvlist{\item " + x["description"],
                    " \href{" + x["href"] + r"}{\textbf{Informacion Aqui}}.}" if x["href"] else r".}",
                    "}"
                ]) for x in self.cfg["experience"]
            )
        )
        with open("cv.tex", "w") as f:
            f.write(data)
        system("bash make")


if __name__ == "__main__":
    from sys import argv
    arg = argv[1:]
    if arg:
        Template().get(arg[0])
