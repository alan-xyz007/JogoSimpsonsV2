import cx_Freeze

executaveis = [
    cx_Freeze.Executable(
        script="main.py",
        icon="assets/icone.ico",
        target_name="JogosMortaisSimpsons.exe"
    )
]

cx_Freeze.setup(
    name="Jogos Mortais - Os Simpsons",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["assets", "recursos"]
        }
    },
    executables=executaveis
)


