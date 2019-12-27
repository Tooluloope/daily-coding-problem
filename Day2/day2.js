const MultiplyArr = (arr) => {
    // Assuming Non zero values
    let s = 1
    for (let i = 0; i < arr.length; i++) {
        s *= arr[i]
        
    }

   let newarr = arr.map((e) => {
      
        return s/e
    });
    return newarr
}

const Multiply = (arr)=> {
    
}

console.log(MultiplyArr([1, 2, 3, 4, 5]))