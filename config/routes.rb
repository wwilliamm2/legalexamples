Rails.application.routes.draw do
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
