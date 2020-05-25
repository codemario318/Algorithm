const anakinSkywalker = 'Anakin Skywalker';
const lukeSkywalker = 'Luke Skywalker';
//
// const obj = {
//   lukeSkywalker,
//   anakinSkywalker,
//   episodeOne: 1,
//   twoJediWalkIntoACantina: 2,
//   episodeThree: 3,
//   mayTheFourth: 4,
// };
//
// console.log(obj.lukeSkywalker);
// obj.lukeSkywalker = 'changed!'
// console.log(obj.lukeSkywalker);
//
function getKey(k) {
  return `a key named ${k}`;
}

// bad
// const obj = {
//   id: 5,
//   name: 'San Francisco',
// };
// obj[getKey('enabled')] = true;
// console.log(obj);
// good
const obj = {
  id: 5,
  name: 'San Francisco',
  ['psble']: true,
};
// obj[getKey('enabled')] = true;
console.log(obj);
console.log(obj['a key named enabled']);
console.log(typeof [getKey('enabled')]);
console.log(typeof ['psble']);
