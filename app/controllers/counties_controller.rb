class CountiesController < ApplicationController
  def listem
  end

  def contra_costa
  end

  def fresno
  end

  def los_angeles
    # Get a unique set of months from a list of files
    @tmp_s_a = []
    File.open("public/lacourt_file_list.txt", "r") do |file|
      file.each_line do |line_s|
        @tmp_s_a = @tmp_s_a + [line_s[0..6]]
      end
    end
    @mmonth_s_a = @tmp_s_a.to_set().to_a().sort
  end
  
  def los_angeles_m
    @mmonth_s = params['mmonth']
    # @mmonth_s = '2024_06'
    # gpt, write demo Ruby syntax to create a regular expression from the string: '2024_06'
    @mmonth_regex = Regexp.new(@mmonth_s)
    @html_f_s_a = []
    File.open("public/lacourt_file_list.txt", "r") do |file|
      file.each_line do |line_s|
        # if regexp made from mmonth_s matches line_s, add line_s to @html_f_s_a
        
        # gpt, write demo Ruby syntax to use a regular expression to
        # match a string named line_s to regexp /2024_06/
        
        if line_s =~ @mmonth_regex #/2024_06/
          @html_f_s_a = @html_f_s_a + [line_s]
        end
        
      end
    end
  end

  def los_angeles_tr
    params['trfile']
    @trfile_regex = Regexp.new(params['trfile'])
    # I should match lines in public/py/tenttext_lacourt14.txt to params['trfile']
    # Know that,
    # I have a python script in public/py which reads filenames from tenttext_lacourt14.txt
    # to generate llm-summaries of the corresponding text files.
    @txt_f_s_a = []
    File.open("public/py/tenttext_lacourt14.txt", "r") do |file|
      file.each_line do |line_s|
        # if regexp matches line_s add line_s to @txt_f_s_a
        if line_s =~ @trfile_regex
          @txt_f_s_a = @txt_f_s_a + [line_s]
        end
      end
    end
  end

  def los_angeles_summ_if
    params['suffix_s_s']
  end
  
  def los_angeles_tr_if
    params['suffix_t_s']
  end
  

  def orange_county
  end

  def riverside
  end

  def sacramento
  end

  def san_bernadino
  end

  def san_luis_obispo
  end

  def san_mateo
  end

  def santa_clara
    @mmonth_s_a = []
    # Get a unique set of months from a list of files
    @tmp_s_a = []
    File.open("public/py/tentpdf_scscourt17.txt", "r") do |file|
      file.each_line do |line_s|
        @tmp_s_a = @tmp_s_a + [line_s[32..38]]
      end
    end
    @mmonth_s_a = @tmp_s_a.to_set().to_a().sort
  end

  def santa_clara_m
    @mmonth_s = params['mmonth']
    @mmonth_regex = Regexp.new(@mmonth_s)
    @pdf_f_s_a = []
    File.open("public/py/tentpdf_scscourt17.txt", "r") do |file|
      file.each_line do |line_s|
        lline_s = line_s.sub('/home/dan/lx/jffj/scscourt/pdfs/','').sub('.pdf','')
        # if regexp made from mmonth_s matches line_s, add line_s to @pdf_f_s_a
        if lline_s =~ @mmonth_regex #/2024_06/
          @pdf_f_s_a = @pdf_f_s_a + [lline_s]
        end
        
      end
    end
  end

  def santa_clara_tr
    params['trfile']
  end

  
  def santa_cruz
  end

  def sonoma
  end
end
