class NPC():
	def __init__(self, arg):
		pass

	def trigger(self):
		if "pickaxe" not in self.parameter['variables']:
			self.conversation_control.print_word("傑克", "終於有人來了！謝謝你救了我！我叫做傑克。","npc_3")
			self.conversation_control.print_word("勇者", "你為什麼會被抓來這裡？","player")
			self.conversation_control.print_word("傑克", "我是一名盜賊，想說可不可以進來這座塔找到一些寶物。\n結果被打暈，醒來就被關來這裡了！","npc_3")
			self.conversation_control.print_word("傑克", "我身上的十字鎬也被拿走了，可不可以請你幫我找我的十字鎬？\n十字鎬上面鑲嵌著紅寶石，很好辨認。","npc_3")
		else:
			self.conversation_control.print_word("傑克", "謝謝你幫我找到十字鎬！我接下來會待在 0 樓\n如果有需要可以讓我幫忙。", "npc_3")
			self.parameter['variables']['Jack_in_B0'] = True
			self.status.expire()