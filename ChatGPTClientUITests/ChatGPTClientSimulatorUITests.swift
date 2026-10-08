import XCTest

final class ChatGPTClientSimulatorUITests: XCTestCase {
    private let fixtureKey = "CHATGPTCLIENT_SIMULATOR_FIXTURE"

    override func setUpWithError() throws {
        continueAfterFailure = false
    }

    func testLaunchListDetailSwitchBackAndRapidReentry() throws {
        let app = launch(mode: "baseline")
        assertListLoaded(app)

        app.staticTexts["Fixture Alpha"].tap()
        XCTAssertTrue(textContaining("Alpha answer 3", in: app).waitForExistence(timeout: 5))
        XCTAssertTrue(textContaining("Alpha heading", in: app).exists)
        backToList(app)

        app.staticTexts["Fixture Beta"].tap()
        XCTAssertTrue(textContaining("Beta answer", in: app).waitForExistence(timeout: 5))
        backToList(app)

        app.staticTexts["Fixture Slow"].tap()
        backToList(app)
        app.staticTexts["Fixture Alpha"].tap()
        XCTAssertTrue(textContaining("Alpha answer 3", in: app).waitForExistence(timeout: 5))
        backToList(app)
        XCTAssertTrue(app.staticTexts["Fixture Beta"].exists)
    }

    func testManualRefreshPersistsCacheAcrossTerminateAndOfflineRelaunch() throws {
        let app = launch(mode: "baseline")
        assertListLoaded(app)
        let refreshButton = app.buttons["Refresh"]
        XCTAssertTrue(refreshButton.waitForExistence(timeout: 3))
        refreshButton.tap()
        XCTAssertTrue(app.staticTexts["Fixture Alpha Refreshed"].waitForExistence(timeout: 5))

        app.terminate()
        app.launchEnvironment[fixtureKey] = "offline-cache"
        app.launch()
        XCTAssertTrue(app.staticTexts["Fixture Alpha Refreshed"].waitForExistence(timeout: 5))
        XCTAssertTrue(app.staticTexts["Fixture Long 1000+"].exists)
    }

    func testLongConversationRoundJumpAndRapidTapsRemainResponsive() throws {
        let app = launch(mode: "baseline")
        assertListLoaded(app)
        app.staticTexts["Fixture Long 1000+"].tap()
        XCTAssertTrue(textContaining("Long answer 502", in: app).waitForExistence(timeout: 10))

        let roundJump = app.buttons["上一轮"]
        XCTAssertTrue(roundJump.waitForExistence(timeout: 5))
        roundJump.tap()
        XCTAssertTrue(textContaining("Long answer 501", in: app).waitForExistence(timeout: 5))
        for _ in 0..<4 { app.buttons["上一轮"].tap() }
        XCTAssertTrue(app.navigationBars["Fixture Long 1000+"].exists || app.staticTexts["Fixture Long 1000+"].exists)
    }

    private func launch(mode: String) -> XCUIApplication {
        let app = XCUIApplication()
        app.launchEnvironment[fixtureKey] = mode
        app.launch()
        return app
    }

    private func assertListLoaded(_ app: XCUIApplication, file: StaticString = #filePath, line: UInt = #line) {
        XCTAssertTrue(app.staticTexts["Fixture Alpha"].waitForExistence(timeout: 5), file: file, line: line)
        XCTAssertTrue(app.staticTexts["Fixture Beta"].exists, file: file, line: line)
        XCTAssertTrue(app.staticTexts["Fixture Slow"].exists, file: file, line: line)
        XCTAssertTrue(app.staticTexts["Fixture Long 1000+"].exists, file: file, line: line)
    }

    private func textContaining(_ value: String, in app: XCUIApplication) -> XCUIElement {
        app.staticTexts.matching(NSPredicate(format: "label CONTAINS %@", value)).firstMatch
    }

    private func backToList(_ app: XCUIApplication, file: StaticString = #filePath, line: UInt = #line) {
        let navigationBar = app.navigationBars.firstMatch
        XCTAssertTrue(navigationBar.waitForExistence(timeout: 2), file: file, line: line)
        let backButton = navigationBar.buttons.firstMatch
        XCTAssertTrue(backButton.exists, file: file, line: line)
        backButton.tap()
        XCTAssertTrue(app.staticTexts["Fixture Alpha"].waitForExistence(timeout: 3), file: file, line: line)
    }
}
