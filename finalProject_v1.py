from breezypythongui import EasyFrame

class theEscape(EasyFrame):

    def __init__(self):
        '''Set up the window and it's widgets'''
        EasyFrame.__init__(self, title = "The Escape", width = 800, height = 600)
        self.setResizable(False)
        
        
        spacerPanelTop = self.addPanel(row = 0, column = 0, columnspan = 3, background = "#1f2022")
        spacerPanelTop.addLabel(text = "Your Adventure Begins", row = 0, column = 0, sticky = "SEW", background = "#1f2022", foreground = "white")
        
        storyPanel = self.addPanel(row = 1, column = 1)
        spacerPanelLeft = self.addPanel(row = 0, column = 0, rowspan = 4, background = "#1f2022")
        spacerPanelRight = self.addPanel(row = 0, column = 2, rowspan = 4, background = "#1f2022")
        spacerPanelMid = self.addPanel(row = 2, column = 0, columnspan = 3, background = "#1f2022")
        choicePanel = self.addPanel(row = 3, column = 1, background = "#1f2022")
        
        spacerPanelBottom = self.addPanel(row = 4, column = 0, columnspan = 3, background = "#1f2022")
        spacerPanelBottom.addButton(text = "Quit", row = 0, column = 0)
        
        self.storyPrompt = storyPanel.addTextArea(text = "You awaken in a dark, dank makeshift dungeon when your senses are assaulted by the overwhelming smell of mildew and sulfur. As you push yourself up off the moist and dingy ground the pain of your body reminds you how you got here in the first place. The pounding in your head berates you for once again spending too much time drinking at the local inn. You look up and see a small beam of moonlight shining in from a crack above. You cannot believe you let yourself get lured in by such an obvious trap. You’re supposed to be the trapper, the scoundrel, the rogue! Pretty women always were your weak point and unfortunately for you all women look pretty with enough mead! You wipe the exhaustion from your eyes and move your hand down to the secret in your pants; no, not that one!  Down to get your trusty old lockpick, of course! You move to the locked gate and have it opened in no time at all. Time to get outta here!", row =  0, column = 0, height = 9, wrap = "word")
        
        
        choicePanel.addButton(text = "1.", row = 0, column = 0)
        self.option1 = choicePanel.addTextArea(text = "Option 1 Goes Here", row = 0, column = 1, height = 1, wrap = "word")
        
        choicePanel.addButton(text = "2.", row = 1, column = 0)
        self.option2  = choicePanel.addTextArea(text = "Option 2 Goes Here", row = 1, column = 1, height = 1, wrap = "word")
        
        choicePanel.addButton(text = "3.", row = 2, column = 0)
        self.option2  = choicePanel.addTextArea(text = "Option 1 Goes Here", row = 2, column = 1, height = 1, wrap = "word")
        
def main():
    theEscape().mainloop()

if __name__ == "__main__":
    main()