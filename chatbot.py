{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "52e5eb06",
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import *\n",
    "\n",
    "root = Tk()\n",
    "root.title(\"Jio Mart Chatbot\")\n",
    "\n",
    "def send_message():\n",
    "    user_input = entry.get().lower()\n",
    "    message = \"\\nYou -> \" + user_input\n",
    "    chat_box.insert(END, message)\n",
    "\n",
    "    if user_input == \"hello\":\n",
    "        bot_response = \"\\nBot -> Hi! How can I assist you?\"\n",
    "    elif user_input == \"browse products\":\n",
    "        bot_response = \"\\nBot -> Sure! Please select a category to browse products.\"\n",
    "        # Implement logic for browsing products\n",
    "    elif user_input == \"add to cart\":\n",
    "        bot_response = \"\\nBot -> Okay! Please provide the details of the item you want to add to your cart.\"\n",
    "        # Implement logic for adding items to cart\n",
    "    elif user_input == \"view cart\":\n",
    "        bot_response = \"\\nBot -> Sure! Here are the items in your cart.\"\n",
    "        # Implement logic for viewing the cart\n",
    "    elif user_input == \"place order\":\n",
    "        bot_response = \"\\nBot -> Great! Please review your order and confirm to proceed.\"\n",
    "        # Implement logic for placing an order\n",
    "    elif user_input == \"track order\":\n",
    "        bot_response = \"\\nBot -> Sure! Please provide your order ID to track your order.\"\n",
    "        # Implement logic for tracking an order\n",
    "    elif user_input == \"cancel order\":\n",
    "        bot_response = \"\\nBot -> We're sorry to hear that you want to cancel your order.\"\n",
    "        bot_response += \"\\nPlease provide your order ID to proceed with the cancellation.\"\n",
    "        # Implement logic for canceling an order\n",
    "    elif user_input == \"talk to customer representative\":\n",
    "        bot_response = \"\\nBot -> You will now be connected to a customer representative.\"\n",
    "        bot_response += \"\\nPlease wait while we connect you...\"\n",
    "        # Implement logic for connecting with a customer representative\n",
    "    else:\n",
    "        bot_response = \"\\nBot -> Sorry, I didn't understand. Can you please repeat?\"\n",
    "\n",
    "    chat_box.insert(END, bot_response)\n",
    "    entry.delete(0, END)\n",
    "\n",
    "# Create chat window\n",
    "chat_box = Text(root)\n",
    "chat_box.grid(row=0, column=0, columnspan=2)\n",
    "\n",
    "# Create input field\n",
    "entry = Entry(root, width=100)\n",
    "entry.grid(row=1, column=0)\n",
    "\n",
    "# Create send button\n",
    "send_button = Button(root, text=\"Send\", command=send_message)\n",
    "send_button.grid(row=1, column=1)\n",
    "\n",
    "root.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d70980ef",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
