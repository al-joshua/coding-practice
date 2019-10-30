"""Add two English words together!

Implement a class Arith (struct struct Arith{value : &'static str,} in Rust) such that

  //javascript
  var k = new Arith("three");
  k.add("seven"); //this should return "ten"
  //c++
  Arith* k = new Arith("three");
  k->add("seven"); //this should return string "ten"
  //Rust
  let c = Arith{value: "three"};
  c.add("seven") // this should return &str "ten"
Input - Will be between zero and ten and will always be in lower case

Output - Word representation of the result of the addition. Should be in lower case"""


class Arith:
    transform_set = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                     'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                     'nineteen', 'twenty']

    def __init__(self, first_word):
        self.first_word = first_word

    def add(self, second_word):
        return self.transform_set[self.transform_set.index(self.first_word) + self.transform_set.index(second_word)]


