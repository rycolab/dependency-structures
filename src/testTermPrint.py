from terms import OrderAnnotation, Term


def main():
    term1 = Term.inner([0, 1, 2, 1], [
        Term.inner([[0], [1]], [Term.leaf()]),
        Term.inner([0, 1], [Term.leaf()])
    ])

    term2 = Term.inner([0, 1, 2], [
        Term.inner([0, 1, 2], [
            Term.inner([0, 1], [Term.leaf()]),
            Term.leaf()
        ]),
        Term.leaf()
    ])

    term3 = Term.inner([0, 1, 2, 3], [
        Term.leaf(),
        Term.inner([1, 0, 2], [Term.leaf(), Term.leaf()]),
        Term.inner([0, 1, 2], [
            Term.inner([1, 0, 1], [
                Term.inner([[0], [1]], [Term.leaf()])
            ]),
            Term.leaf()
        ])
    ])

    term4 = Term.inner([0, 1, 2], [
        Term.leaf(),
        Term.inner([[0, 1, 2, 1, 2], [1, 2]], [Term.leaf(), Term.leaf()])
    ])

    term5 = Term.inner([0, 1, 2, 3], [
        Term.inner([[0], [1]], []),
        Term.leaf(),
        Term.inner([[1], [0]], []),
    ])

    term6 = Term.inner([[0, 1, 2, 1, 2], [3, 4, 5, 6]], [
        Term.leaf(),
        Term.leaf()
    ])

    term7 = Term.inner([0, 1], [])
    term8 = Term.inner([0, 1, 0], [])

    print(term1, '\n')
    print(term2, '\n')
    print(term3, '\n')
    print(term4, '\n')
    print(term5, '\n')
    print(term6, '\n')
    print(term7, '\n')
    print(term8, '\n')


if __name__ == '__main__':
    main()
