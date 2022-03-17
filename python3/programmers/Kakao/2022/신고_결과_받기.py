from collections import defaultdict


def solution(userIds, report, k):
    deduplicateReport = set(report)

    reportResult = getReportResult(deduplicateReport)
    sendMailCounts = getSendMailCounts(reportResult)

    return [sendMailCounts[userId] for userId in userIds]


def getReportResult(report):
    reportResult = defaultdict(list)

    for r in report:
        reportingUserId, reportedUserId = r.split(' ')
        reportResult[reportedUserId].append(reportingUserId)

    return reportResult


def getSendMailCounts(reportResult, k):
    sendMailCounts = defaultdict(int)

    for reportingUsers in reportResult.values():
        reportCount = len(reportingUsers)

        if reportCount < k:
            break

        for reportingUser in reportingUsers:
            sendMailCounts[reportingUser] += 1

    return sendMailCounts
