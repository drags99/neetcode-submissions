impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        
        if nums.len() == 0 {
            return false
        }

        // simple case when len nums is 0, return false
        let mut seen: Vec<i32> = Vec::<i32>::new();
        let mut nums = nums.clone();
        
        nums.sort();

        let iternum = nums.iter();

        for i in iternum {
            if seen.contains(i) {
                return true;
            } else {
                seen.push(i.clone());
            }
        };

        return false;
    }
}
