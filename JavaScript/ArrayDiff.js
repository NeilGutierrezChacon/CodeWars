function arrayDiff(a, b) {
  b.forEach((element) => {
    a = a.filter((value, index, array) => {
      return value != element;
    });
  });
  return a;
}

console.log(arrayDiff([], [4,5]));

console.log(arrayDiff([3,4], [3]));

console.log(arrayDiff([1,8,2], []));

/* END */