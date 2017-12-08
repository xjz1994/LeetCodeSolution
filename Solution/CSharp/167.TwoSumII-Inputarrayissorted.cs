		static public int[] TwoSum(int[] numbers, int target) {
		    if (numbers == null || numbers.Length < 1) {
		        return null;
		    }
		    int right = numbers.Length - 1;
		    while (left < right) {
		        if (numbers[left] + numbers[right] > target) {
		            right--;
		        } else if (numbers[left] + numbers[right] < target) {
		            left++;
		        } else if (numbers[left] + numbers[right] == target) {
		            int[] result = { left + 1, right + 1 };
		            return result;
		        }
		    }
		    return null;
		}