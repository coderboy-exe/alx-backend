var kue = require('kue');

const queue = kue.createQueue();

const jobData = {
	phoneNumber: '123456789',
	message: 'This is the code to verify your account',
}

const job = queue.create('push_notification_code', jobData).save( (err) => {
	if (!err) {
	  console.log('Notification job created:', job.id)
	}
});

job.on('complete', (result) => {
  console.log('Notification job completed');

}).on('failed', (error) => {
  console.log('Notification job failed');

})
