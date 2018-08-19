from django.db import models
from shop.models import Product

# Create your models here.

class Order(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	address = models.CharField(max_length=250)
	postal_code = models.CharField(max_length=20)
	city = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	#[Modified] New attributes...
	MODE_CHOICES = (
		('cash', 'Cash',),
		('paypal', 'PayPal',),
	)
	CLAIM_CHOICES = (
		('delivery', 'Delivery',),
		('pickup', 'Pickup',),
	)
	mode = models.CharField(max_length=10, choices=MODE_CHOICES,
		default='paypal')
	claim = models.CharField(max_length=10, choices=CLAIM_CHOICES,
		default='delivery')
	
	"""MODE_CHOICES = (
		('cod', 'Cash on Delivery',),
		('cop', 'Cash on Pickup',),
		('ppd', 'PayPal on Delivery',),
		('ppp', 'PayPal on Pickup',),
	)

	mode = models.CharField(max_length=10, choices=MODE_CHOICES,
		default='cod')"""

	paid = models.BooleanField(default=False)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return 'Order {}'.format(self.id)

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items')
	product = models.ForeignKey(Product, related_name='order_items')
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return '{}'.format(self.id)

	def get_cost(self):
		return self.price * self.quantity
