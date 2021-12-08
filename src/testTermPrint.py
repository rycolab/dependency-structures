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

    print(term3)


if __name__ == '__main__':
    main()
