def Grid(n_rows, n_coloumns, size):
    decor = "#"+"#"*(size+1)*n_coloumns
    row =("\n"+(("#"+" "*size))*n_coloumns+"#")*size
    print(decor+(row+"\n"+decor)*n_rows)

(n_rows, n_coloumns, size) = [int(num) for num in input().split(" ")]

Grid(n_rows, n_coloumns, size)
        