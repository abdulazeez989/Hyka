class Tab(FloatLayout, MDTabsBase):
	screen_manager=ObjectProperty()
	main_page=ObjectProperty()
	green_md_tab=ObjectProperty()
	tab_tab=ObjectProperty()
class MainApp(MDApp):
	count_one=0
	count_main=0
	count_two=0
	#methods
	def on_start(self):
		anim =Animation(size=(798, 1298), duration=1.) + Animation(size=(800, 1300), duration=1.)
		anim.repeat=True
		db=self.root.ids.main_page
		anim.start(db)
		
		b=self.root.screen_manager
		b.current='f1_screen'
		
		#Clock counter
		Clock.schedule_interval(self.start_screen_one, 2)
		
	def start_screen_one(self, *args):
		
		self.count_one=self.count_one+1
		if self.count_one==2:
			
			b=self.root.screen_manager
			b.current='f2_screen'
			b.transition.direction='left'
			
			
		Clock.schedule_interval(self.start_screen, 2)
		
	def start_screen(self, *args):
		self.count_two=self.count_two+1
		if self.count_two==2:
			
			b=self.root.screen_manager
			b.current='f3_screen'
			b.transition.direction='right'
		
		Clock.schedule_once(self.start_main_screen, 2)
		
	def start_main_screen(self, *args):
		
		self.count_main=self.count_main+1
		if self.count_main==2:
			
			b=self.root.screen_manager
			b.current='main_screen'
			b.transition.direction='right'
			
	def on_tab_switch(self, *args):
		data=["brown", "green", "lightgreen", "silver", "lightblue", "orange"]
		a=random.randint(0, 7)
		if a==1:
			self.root.ids.green_md_tab.background_color=data[0]
			
		elif a==2:
			self.root.ids.green_md_tab.background_color=data[1]
			
		elif a==3:
			self.root.ids.green_md_tab.background_color=data[2]
			
		elif a==4:
			self.root.ids.green_md_tab.background_color=data[3]
			
		elif a==5:
			self.root.ids.green_md_tab.background_color=data[4]
			
		else:
			self.root.ids.green_md_tab.background_color=data[5]
			
	def build(self):
		#return screen
		return Builder.load_string(KV)
		
MainApp().run()
