# letters should be a Python list where each entry is an uppercase letter of the English alphabet. For instance, the first two entries should be "A" and "B", and the final two entries should be "Y" and "Z". Use the string alphabet to create this list.
# address should be a Python list where each row in address is a different item in the list. Currently, each row in address is separated by a comma


alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
address = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"

# TODO: Convert strings into Python lists
words_in_alphabet = alphabet.split(".")
address_parts = address.split(",")
print(words_in_alphabet)
print(address_parts)