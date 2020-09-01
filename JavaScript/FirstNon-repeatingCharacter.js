function firstNonRepeatingLetter(s) {
  for (i = 0; i < s.length; i++) {
    let cont = 0;
    for (j = 0; j < s.length; j++) {
      if (s[i].toLowerCase() == s[j].toLowerCase()) cont++;
    }
    if (cont <= 1) {
      return s[i];
    }
  }
  return "";
}

console.log(firstNonRepeatingLetter("a"));
console.log(firstNonRepeatingLetter("stress"));
console.log(firstNonRepeatingLetter("moonmen"));

/* END */
