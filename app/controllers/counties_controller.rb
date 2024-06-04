class CountiesController < ApplicationController
  def listem
  end

  def contra_costa
  end

  def fresno
  end

  def los_angeles
  end

  def los_angeles_m
    @html_f_s_a = []
    File.open("public/lacourt_file_list.txt", "r") do |file|
      file.each_line do |line|
        @html_f_s_a = @html_f_s_a + [line]
      end
    end
  end

  def los_angeles_tr
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
  end

  def santa_cruz
  end

  def sonoma
  end
end
