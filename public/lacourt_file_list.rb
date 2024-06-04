# ~/lx/lx14/public/lacourt_file_list.rb

# gpt,
# write demo Ruby syntax which uses a loop to read and print each line in a text file.
# gpt,
# Python allows me to use the `with` command to open 'hello.txt', operate on hello.txt, and then close hello.txt. I like the Python `with` command because it offers nice clean-up behavior. Does Ruby offer a similar mechanism when I use Ruby to operate on hello.txt?

File.open("hello.txt", "r") do |file|
  # Operate on the file
  file.each_line do |line|
    # Process each line
    print line
  end
end

File.open("lacourt_file_list.txt", "r") do |file|
  # Operate on the file
  file.each_line do |line|
    # Process each line
    print line
  end
end

