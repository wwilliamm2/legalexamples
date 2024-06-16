Rails.application.routes.draw do
  get 'counties/listem'
  get 'counties/contra_costa'
  get 'counties/fresno'
  get 'counties/los_angeles'

  get 'counties/los_angeles_m/:mmonth',  to: 'counties#los_angeles_m'
  get 'counties/los_angeles_tr/:trfile', to: 'counties#los_angeles_tr'
  get 'counties/los_angeles_summ_if/:suffix_s_s', to: 'counties#los_angeles_summ_if'
  get 'counties/los_angeles_tr_if/:suffix_t_s', to: 'counties#los_angeles_tr_if'
  
  get 'counties/orange_county'
  get 'counties/riverside'
  get 'counties/sacramento'
  get 'counties/san_bernadino'
  get 'counties/san_luis_obispo'
  get 'counties/san_mateo'

  get 'counties/santa_clara'
  get 'counties/santa_clara_m/:mmonth',  to: 'counties#santa_clara_m'

  get 'counties/santa_cruz'
  get 'counties/sonoma'
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html
  get 'home/about'
  get 'home/blog'
  get 'home/contact'
  get 'home/doctype'
  get 'home/tech'

  get  '/about',   to: 'home#about'
  get  '/blog',    to: 'home#blog'
  get  '/contact', to: 'home#contact'
  get  '/doctype', to: 'home#doctype'
  get  '/tech',    to: 'home#tech'


  # Reveal health status on /up that returns 200 if the app boots with no exceptions, otherwise 500.
  # Can be used by load balancers and uptime monitors to verify that the app is live.
  get "up" => "rails/health#show", as: :rails_health_check

  # Defines the root path route ("/")
  root "home#about"
end
