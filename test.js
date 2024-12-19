const removeItemAtIndex = (list, index) => {
    console.log([...list].slice(0, index));
    console.log([...list].slice(index + 1));
    return [...list].slice(0, index) + [...list].slice(index + 1);
};

const test = ['a', 'b', 'c', 'd', 'e'];

console.log(removeItemAtIndex(test, 2));
console.log('hello')

console.log(['a', 'b'] + ['d', 'e'])