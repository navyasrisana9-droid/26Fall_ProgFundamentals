item_name = "Notebook"
unit_price = 2.50
quantity = 4

subtotal = unit_price * quantity
tax_amount = subtotal * 0.05
final_total = subtotal + tax_amount

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax Amount: ${tax_amount:.2f}")
print(f"Final Total: ${final_total:.2f}")