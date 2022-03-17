function solution(userIds, reports, k) {
    const deduplicateReport = new Set(reports);
    const reportPairs = getReportPairs(deduplicateReport);
    const reportResult = getReportResult(reportPairs);
    const mailCounts = getMailCounts(k, reportResult);
    const mailSummary = mailCountsToArray(userIds, mailCounts);
    return mailSummary;
}

function getReportPairs(reports) {
    const reportPairs = [];
    reports.forEach(report => reportPairs.push(report.split(' ')));
    return reportPairs;
}

function getReportResult(reportPairs) {
    const reportResult = new Map();

    reportPairs.forEach(report => {
        const [reportingUserId, reportedUserId] = report;
        const reportingUserIds = reportResult.has(reportedUserId) ? reportResult.get(reportedUserId) : [];

        reportingUserIds.push(reportingUserId);
        reportResult.set(reportedUserId, reportingUserIds);
    })

    return reportResult;
}

function getMailCounts(k, reportResult) {
    const mailCounts = new Map();
    const reports = Array.from(reportResult.values()).filter(report => report.length >= k);
    
    reports.forEach(reportingUserIds => {
        reportingUserIds.forEach(reportingUserId => {
            const count = mailCounts.has(reportingUserId) ? mailCounts.get(reportingUserId) + 1 : 1;
            mailCounts.set(reportingUserId, count);
        })
    })

    return mailCounts;
}

function mailCountsToArray(userIds, mailCounts) {
    return userIds.map(userId => mailCounts.has(userId) ? mailCounts.get(userId) : 0);
}

const userIds = ["muzi", "frodo", "apeach", "neo"],
      report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
      k = 2;

console.log(solution(userIds, report, k));