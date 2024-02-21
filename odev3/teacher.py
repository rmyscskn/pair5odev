class Teacher:
    def __init__(self, name,lastName, branch):
        self.name = name
        self.lastName = lastName
        self.branch = branch

    def information(self):
        return f"Öğretmen bilgisi: {self.name} {self.lastName} {self.branch}"

    def get_branch(self):
        return self.branch









