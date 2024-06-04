# ~/lx/lx14/public/get_yr_mmonth.rb


@yr_mmonth_s_a = []
File.open("public/lacourt_file_list.txt", "r") do |file|
  file.each_line do |line_s|
    @yr_mmonth_s_a = @yr_mmonth_s_a + [line_s[0..6]]
  end
end

# gpt, In Python I can create a Set of unique elements from a List like this: myset = set([1,1,2,2]). How do I do something similar in Ruby? Write demo Ruby syntax which transforms a Ruby array [1,1,2,2] into an array of unique elements: [1,2]

@yr_mmonth_s_st = @yr_mmonth_s_a.to_set()
print @yr_mmonth_s_st


