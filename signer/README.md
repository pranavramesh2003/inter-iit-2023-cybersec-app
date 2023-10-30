# signer

You are given a signer library (`signer.py`) which can generate signatures for
data and verify these signatures. Your job is to generate a signature for any
data which has `"InterIIT-2023"` in it.

The catch here is that the library won't let you generate the signature for any
data which has `"InterIIT-2023"` in it. So you have to come up with a clever way
to get the library to generate a signature for such data, and prove it by
verifying it. You goal is hence to make the `Signer.execute` function return
`(2,"Congratulations, you did it!")`.

You should implement a solution script in `runner.py`.

**Caution**: Make sure you read all the comments in `runner.py`. If your code
does not obey the constraints mentioned in the file, then your solution for this
challenge would be disqualified.
