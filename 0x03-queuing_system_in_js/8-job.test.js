var kue = require('kue');
import { expect } from 'chai';
import { describe, it, before, afterEach, after } from 'mocha';
import createPushNotificationsJobs from './8-job'

const queue = kue.createQueue();

describe("createPushNotificationsJobs", () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it("Should throw an error if jobs is not an array", () => {
    expect(() => {
      createPushNotificationsJobs(null, queue);
    }).to.throw("Jobs is not an array");
  });

  it('Should create new indiviaual jobs from array', () => {
    const jobs = [
      {
        phoneNumber: '0123456789',
        message: 'Test data 1'
      },
      {
        phoneNumber: '5678912345',
        message: 'Test data 2'
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.equal(jobs[0]);
    expect(queue.testMode.jobs[0].data.message).to.equal('Test data 1');

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.equal(jobs[1]);
    expect(queue.testMode.jobs[1].data.message).to.equal('Test data 2');
  });
});
