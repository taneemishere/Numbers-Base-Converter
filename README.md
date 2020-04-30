# Numbers Base Converter

A Python application that can convert a number from one base to another.
Keep in mind that when to convert from base N to base 10 we use the multiplication method. For example 621 in base 8 when to convert to base 10 we should do it as: 
6*(8^2) + 2*(8^1) + 1*(8^0).

And when to convert from base 10 to base N, we should use the reapeated divsion method in which the number is repeatidly divided by the number to which we're converting until we reach to zero. And the decimal part is multiplied by that N base's number. And the result should be considered from bottom to top. For example when to convert 22 in base 10 to base 8, it can be done as, 22/8 = 2.75, now 0.75x8 = 6, then 2/8 = 0.25, now 0.25x8 = 2, then 0/8 and here we get zero so we stopped, and the result is 26 in base 8.

## Getting Started

To get things started, you need to install Python in your computer and BOOM you're ready.

## The Code

Below are the methods and their workings.

```
def check_binary(check_number):
```

As sets cannot hold multiple instances of an item, so if we convert it into sets so we can remove duplicates.

```
[int(item) for item in set(list(check_number))]
```

Pass the string from user and convert it into integer. int(item) and then we can check a string against ‘0’ and  ‘1’ . That means check the 0 or 1, if it is in [0, 1] it’s fine otherwise it’ll return False

```
def check_input(input_number):
```

This checks if the input belongs to the define character set char_list.

```
def check_validity(input_number, input_base, output_base):
```

First checks if user entered a number (digit) or a HEX value
Then check the bases. Correspondingly changing it into, what the user entered in input_base, 2, 8, 16 and so on.
Then check whether the user wants to convert to or from the base 1, which shows an error statement of can’t convert to or from base 1.

```
def main_converter(input_number, input_base, output_base):
```

In this method the

```
Reaminder_list[]
```

is holding the number we want to return at the end. And

```
int_base_10
```
considering the base 10 as an intermediate base while converting from N to N base.

### Binary Output

The if condintion looks for the validity of the binary numbers and then the bin() returns the ob followed by the binary number. So we use the [2:].

### When base is NOT 10

If the base is NOT 10 we use the intermediate step. Reverse the list by 

```
reversed_input_number = input_number[::-1]
```

The hex_helper_dict, help us in controlling the numbers above 9 if we receive a HEX value in input. Now for this we’ll use the Multiplication Process. E.g. 
1(8^2) + 2(8^1) + 3(8^0) = 64 + 16 + 3 = 83. 
83 is in decimal now, from 123 in octal. And same for the HEX numbers, 10 is A, 11 is B up to 15 is F.

### When base is 10

When input_base is 10, so we use our repeated division method until we come to zero. The // use for the floor division. And the part after the decimal point, we get by the % sign, actually the remainder, this is to appended to the remainder_list so it can be displayed.

### When output base is 16

If we get the output_base, 16 so then we should convert the numbers above 9 to it alphas. And as we did earlier use the dictionary hex_dict, if we find, convert and append to list.

Then at last,

```
return ''.join(remainder_list[::-1])
```

Finally,

```
def main_menu():
```

This interacts with the user to take input number and base, output base and showing the outputs. And we iterated in while loop until the user didn’t enter the ‘n’ while asking by the loop.

## Run

Run the main.py and so you'll have your own Number Base Converter running in your terminal.

## Thanks to

Thanks to Martin Andersson Aaberge for sharing his math to us.

Please read [this article](https://towardsdatascience.com/how-to-write-a-number-systems-calculator-in-python-b172557cb705) for the original idea.

## License

This project is licensed under the MIT Open Source License.
