const twosum = (arr, k) => {
    for (let i = 0; i < arr.length; i++) {
        if ( arr.slice(i+1).includes(k- arr[i])) {
            return true
        }
        
        
    }
    return false
}

const twosum1 = (arr,k) => {
    dict = {}
    for(let i = 0; i < arr.length; i++){
        if (dict.include(arr[i])){
            return true
        }
        else {
            dict[k-arr[i]] = i
        }
    }
    return false
}
console.log(twosum([10, 15, 3, 7], 17))