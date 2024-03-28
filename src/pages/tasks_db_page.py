from src.actions import Actions

class TaskDbPage(Actions):
    
     # ----------------------- HELPERS ------------------------
    def path_div_task_card(self):
        """
        Returns path of a task card
        """
        
        path = "//div[contains(@id, 'items')]/div[contains(@class, 'col')]" + \
            "//div[contains(@class, 'card') and @draggable]"
    
        return path
    

     # ----------------------- VALIDATE ------------------------

    def validate_div_task_cards(self, task_cards, check_order=False, exists=True):
        """
            Validates task cards
            @param task cards = list with the names of task cards we want to validate
            @pram check_order: boolean. If True the alphabetical order of cards is checked 
        """
        path_0 = self.path_div_task_card()
        list_to_check = []
        index = 1
        
        for task in task_cards:       
            if check_order:
                path = path_0  + "[" + str(index) + "]" + "[contains(.,'" + str(task) + "')]"

                index += 1
            else:          
                path = path_0 + "[contains(.,'" + str() + "')]"
                
            # Append list of paths for further checking
            list_to_check.append(path)
            
        # Validate each  path of the list
        for path_item in list_to_check:
            self.existence(path_item, exists=exists)
    
   # ----------------------- CLICK ------------------------
    def click_a_sort_by_summary_btn(self):
        """
            Clicks the sort by summary arrow button
        """
        path = f"//div[contains(@id, 'sort')]//a"
        self.find_and_click(path)
    
    def click_a_sort_by_summary_arrow_btn(self, arrow="up"):
        """
            Clicks the sort by summary arrow button
            @param arrow: arrow direction ("up" or "down")
        """
        path = f"//div[contains(@id, 'sort')]//a[//i[contains(.,'{arrow}')]]"
        self.find_and_click(path)
        
        
        