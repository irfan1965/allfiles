l=[
[[570, 600], [660, 769], [840, 1110]],
[[540, 615], [630, 700], [780, 1080]],
[[480, 540], [570, 772], [820, 1035]],
]
for x,i in enumerate(self.Timings):
            if mst in range(i[0], i[1]):
                if mst == i[0]:
                    i[0] = mend
                elif mend == i[1]:
                    i[1] = mst
                else:
                    self.Timings.append([i[0], mst])
                    self.Timings.append([mend, i[1]])
                    del self.Timings[x]
