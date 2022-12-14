##this O(n) time complexity since there is one for loop which runs for n times
def count_batteries_by_usage(cycles):
  ##this is initialization part
  lowCount=0
  mediumCount=0
  highCount=0
  for battery in cycles:
    if(battery<410):                        ##if batteries are charged less than 410 times it is classified as low
      lowCount+=1
    elif(battery>=410 and battery<=909):    ##if batteries are charged between 410 times to 909 times it is classified as medium
      mediumCount+=1
    else:                                   ##if batteries are charged greater than 909 times it is classified as high
      highCount+=1
  return {
    "lowCount": lowCount,                    ##here we are returning a dictionary od number of batteries classified as low, medium and high
    "mediumCount":mediumCount,
    "highCount": highCount
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  ## here we are adding additional test cases to check for boundary value cases 
  counts = count_batteries_by_usage([0,409,410,660,909,910,911])  ##here we have selected battery values using minimum,minimun+1,maximum,maximum-1,nominal values.
  ## here are expected output for the above test cases 
  ##assert(counts["lowCount"] == 2)
  ##assert(counts["mediumCount"] == 3)
  ##assert(counts["highCount"] == 1)
  counts = count_batteries_by_usage([210,610,910]) ## here we have selected battery values using equivalence class testing .
  ##here are expected output for the above test cases 
  ##assert(counts["lowCount"] == 1)
  ##assert(counts["mediumCount"] == 1)
  ##assert(counts["highCount"] == 1)

  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
